# linreg.r

# This script should do linear regression.
# Demo:
# R -f linreg.r

csv_l = read.csv('somepredictions.csv')
head(csv_l)
summary(csv_l$pctlag1)

x_l = csv_l[ , c(4:6)]
head(x_l)
summary(x_l)

