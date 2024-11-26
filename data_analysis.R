# Question b
education = read.table("C:/Users/Juan Kim/R/education.dat", header = T)
education[1:10,]

# Question c
divided = cut(education$Tutoring_time, breaks = seq(0,50,10), right=FALSE)
table(divided)
hist(education$Tutoring_time, breaks = seq(0, 50, 10), right = FALSE, 
     main = "Histogram of Frequencies for Turoting Time", xlab= "Average Amount of Tutoring Time per Week")

# Question d
table(education$Major)
barplot(table(education$Major), main = "Job Field Preference", xlab = "Job Fields", ylab = "Frequency")
legend("topleft", 
       legend = c("1 - 교육계열", 
                  "2 - 예술 및 인문학", 
                  "3 - 사회과학, 언론 및 정보학", 
                  "4 - 경영, 행정 및 법", 
                  "5 - 자연 과학, 수학 및 통계학", 
                  "6 - 정보통신기술", 
                  "7 - 공학, 제조 및 건설", 
                  "8 - 농림어업 및 수의학", 
                  "9 - 보건 및 복지", 
                  "10 - 서비스", 
                  "11 - 기타(아직 결정 안함, 진학 안함 등)"), 
       title = "Job Fields", box.lty = 1, cex = 0.5)

# Question e
table(education$Income)
hist(education$Income, breaks = seq(1, 9, 1), right = FALSE, 
     main = "Histogram of Frequencies for Income", xlab= "Income(1 million KRW)")

# Question f
df1 = data.frame(education$Afterschool, education$Region)
dft1 = table(df1)
colnames(dft1) <- c("서울", "광역시", "중소도시", "읍면지역")
barplot(dft1, ylab = "Frequency", xlab = "Region", 
        main = "Side-By-Side Bar Chart", col = c("yellow", "blue"), beside = TRUE)
legend("topleft", legend = c("참여", "미참여"), fill = c("yellow", "blue"), title = "Opinion", box.lty = 1)

# Question g
reg1 = subset(education, Region == 1)$Tutoring_time
reg2 = subset(education, Region == 2)$Tutoring_time
reg3 = subset(education, Region == 3)$Tutoring_time
reg4 = subset(education, Region == 4)$Tutoring_time

par(mfrow = c(2, 2))

hist(reg1, breaks = seq(0, 50, 10), right = FALSE, 
     main = "Histogram of Frequencies for Tutoring Time", 
     xlab = "Tutoring Time (서울)", col = "lightblue")

hist(reg2, breaks = seq(0, 50, 10), right = FALSE, 
     main = "Histogram of Frequencies for Tutoring Time", 
     xlab = "Tutoring Time (광역시)", col = "lightgreen")

hist(reg3, breaks = seq(0, 50, 10), right = FALSE, 
     main = "Histogram of Frequencies for Tutoring Time", 
     xlab = "Tutoring Time (중소도시)", col = "lightcoral")

hist(reg4, breaks = seq(0, 50, 10), right = FALSE, 
     main = "Histogram of Frequencies for Tutoring Time", 
     xlab = "Tutoring Time (읍면지역)", col = "lightyellow")

par(mfrow = c(1, 1))

# Question h
plot(education$Tutoring_time, education$Tutoring_amount, main = "Scatterplot", xlab = "Tutoring Time per Week", ylab = "Tutoring Expenditure per Month (1000 KRW)")

# Question i
data = education$Tutoring_amount
mean(data)
median(data)
quantile(data)
IQR(data)
sd(data)
diff(range(data))

plot(data)