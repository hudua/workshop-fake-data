data <- read.csv("program_costs.csv")


group1 <- data$ApplicationCost[1:10]
group2 <- data$ApplicationCost[11:20]




t_test_result <- t.test(group1, group2, alternative = "two.sided", var.equal = FALSE)

print(t_test_result)


library(haven)
write_sas(data, 'output.sas7bdat')


df <- read_sas("output.sas7bdat")
df
