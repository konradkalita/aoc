import qualified Data.Set as S
import Data.Function ((&))

toInt ('+':n) = read n
toInt n = read n

duplicates xs =
    dups xs S.empty
    where dups (y:ys) s | S.member y s = (y:dups ys s) | otherwise = dups ys (S.insert y s)

accum = scanl (+) 0

main = do
    input <- map toInt . lines <$> readFile "2018/day01/in.txt"
    print $ sum input
    print $ input & cycle & accum & duplicates & head