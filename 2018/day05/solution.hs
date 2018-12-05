import Data.Char(toLower)

opposite x y = x /= y && toLower x == toLower y

collapse = (-2+) . length . foldl (\(x:xs) y -> if opposite x y then xs else y:x:xs) ['-']

main = do
    ss <- readFile "2018/day05/in.txt"
    print $ collapse ss