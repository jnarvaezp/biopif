# read information in the output file from hmmscan and generate image

args <- commandArgs(TRUE)
file <- args[1]
print (file)

data <- read.table("output", sep = "\"",
    header = TRUE, )

# return maximum sequence length

maxlen <- max(data$len)
#
# identify number of proteins

prots <- length(levels(data$protname))
lol<-paste(file,"png", sep=".")
png(lol)
plot(0, type = "n", xlim = c(-300, maxlen + 100),
    ylim = c(0, prots + 2), xlab = "POS", ylab = "", yaxt = "n",
    main = "Domain architecture of clotting proteins")
prevname <- ""
y <- 1
width <- 0.02
palette(rainbow(7))
lines <- length(data$protname)

for (i in (1:lines)) {

    test <- data$protname[i]
    if (test != prevname) {
        y <- y + 1
        # print protein names at y axis
        text(-10, y, data$protname[i], cex = 0.7, pos = 2)
        # draw lines corresponding to the protein lengths
        lines(c(1, data$len[i]), c(y, y), col = "grey", lw = 2)
    }
    prevname <- test


    # draw domain rectangles
    domlen <- length(levels(data$domname))
    # assign a colour to the domain
    for (k in (1:domlen)) {
        if (levels(data$domname)[k] == data$domname[i]) {
            color <- k
        }
    }
    ybottom <- y - width * color
    ytop <- y + width * color
    rect(data$begin[i], ybottom, data$end[i], ytop, col = color)
}

# Finally draw the domain information in a separate panel

x <- maxlen * 0.7
for (k in (1:domlen)) {
    pos <- 4 + k * 0.8
    rect(x, pos - 0.02 * k, x + 100, pos + 0.02 * k, col = k)
    text(x + 100, pos, levels(data$domname)[k], pos = 4, cex = 0.7)

}


dev.off()