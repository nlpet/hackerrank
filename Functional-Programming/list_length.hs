--Only fill up the blanks for the function named len
--Do not modify the structure of the template in any other way
len :: [a] -> Int
len lst = sum [1 | i <- [1..length lst]]

-- alternative
len' = sum . map (\x -> 1)
