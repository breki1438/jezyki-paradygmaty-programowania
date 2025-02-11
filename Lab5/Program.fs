open System

//Zad1
let rec fibonacci n =
    if n <= 1 then n
    else fibonacci (n - 1) + fibonacci (n - 2)

let fibonacciTailRec n =
    let rec loop n a b =
        if n = 0 then a
        else loop (n - 1) b (a + b)
    loop n 0 1

//Zad2
type Tree<'T> =
    | Empty
    | Node of 'T * Tree<'T> * Tree<'T>

let rec searchTree value tree =
    match tree with
    | Empty -> false
    | Node (v, left, right) ->
        if value = v then true
        else searchTree value left || searchTree value right

let searchTreeIterative value tree =
    let rec loop stack =
        match stack with
        | [] -> false
        | Empty :: rest -> loop rest
        | Node (v, left, right) :: rest ->
            if v = value then true
            else loop (left :: right :: rest)
    loop [tree]

//Zad3
let rec permutations lst =
    match lst with
    | [] -> [[]]
    | _ ->
        lst |> List.collect (fun x ->
            permutations (List.filter ((<>) x) lst)
            |> List.map (fun perm -> x :: perm))