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
typeof(x_l)

y_is = csv_l[ , 3]
head(y_is)

# Now I should learn:
mymodel = lm(y_is ~ pctlag1 + pctlag2 + pctlag4, data=x_l)
mymodel

# Now I should predict one observation:
firstx = x_l[1,]
aprediction = predict(mymodel,firstx)
aprediction

# Now I should predict one observation (quiet day):
just1x = list(pctlag1=0.001,pctlag2=0.001,pctlag4=0.001)
aprediction = predict(mymodel,just1x)
aprediction

# Now I should predict one observation (strong down day):
just1x = list(pctlag1=-2.1,pctlag2=-3.1,pctlag4=-3.2)
aprediction = predict(mymodel,just1x)
aprediction

# Now I should predict one observation (strong up day):
just1x = list(pctlag1=2.1,pctlag2=2.4,pctlag4=3.2)
aprediction = predict(mymodel,just1x)
aprediction
