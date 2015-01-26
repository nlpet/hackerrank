

# Enter your code here. Read input from STDIN. Print output to STDOUT
nums <- read.table("/dev/stdin", sep=" ");
nums <- as.list(as.data.frame(t(nums)))
write.table(as.numeric(nums[1])+as.numeric(nums[2]), sep = "", append=T, row.names = F, col.names = F)