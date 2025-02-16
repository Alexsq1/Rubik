--This program calculates the number of different states of a nxnxn Rubik's Cube

main :: IO()
main = do
    putStrLn "This program calculates the number of different states of a nxnxn Rubik's Cube :D."
    putStrLn "Insert the number of n:"
    input <- getLine
    let n = read input :: Integer
    putStrLn $ "Number of states is " ++ (show $ states n)
    putStrLn $ "This number has " ++ (show $ numDigits $ states n) ++ " digits"
    return ()


states :: Integer -> Integer
states n
    | n == 1 = 1
    | n <= 0 = 0
    | parity == 0 = div (((!)7) * (3 ^ 6) * (((!)24) ^ (k * (k-1))) ) (((!)4) ^ (6* ((k-1)^2)) )
    | parity == 1 = div (((!)8) * (3 ^ 7) * ((!)12) * (2^10)* (((!)24) ^ ((k+1) * (k-1))) ) (((!)4) ^ (6* (k*(k-1))) )
    | otherwise = 0

    where
        (k, parity) = n `quotRem` 2

--We express n = 2*k + parity

(!) :: Integer -> Integer
(!) n 
    | n <= 1 = 1
    | otherwise = product [2 .. n]

numDigits :: Integer -> Integer
numDigits n
    | n == 0 = 1
    | otherwise = floor(1 + logBase 10 (fromInteger $ abs n))

