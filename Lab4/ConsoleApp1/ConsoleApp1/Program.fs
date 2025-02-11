open System

// Zadanie 1
let calculateBMI weight height =
    let heightM = height / 100.0
    let bmi = weight / (heightM * heightM)
    let category =
        if bmi < 18.5 then "Niedowaga"
        elif bmi < 24.9 then "Normalna waga"
        elif bmi < 29.9 then "Nadwaga"
        else "Otyłość"
    bmi, category

let bmiApp () =
    printf "Podaj wagę (kg): "
    let weight = Console.ReadLine() |> float
    printf "Podaj wzrost (cm): "
    let height = Console.ReadLine() |> float
    let bmi, category = calculateBMI weight height
    printfn "Twoje BMI: %.2f, Kategoria: %s" bmi category

// Zadanie 2
let exchangeRates =
    Map ["USD", 1.0; "EUR", 0.85; "GBP", 0.75]

let convertCurrency amount fromCurrency toCurrency =
    match Map.tryFind fromCurrency exchangeRates, Map.tryFind toCurrency exchangeRates with
    | Some fromRate, Some toRate -> Some (amount * (toRate / fromRate))
    | _ -> None

let currencyConverterApp () =
    printf "Podaj kwotę: "
    let amount = Console.ReadLine() |> float
    printf "Podaj walutę źródłową (USD/EUR/GBP): "
    let fromCurrency = Console.ReadLine().ToUpper()
    printf "Podaj walutę docelową (USD/EUR/GBP): "
    let toCurrency = Console.ReadLine().ToUpper()
    match convertCurrency amount fromCurrency toCurrency with
    | Some result -> printfn "Kwota po konwersji: %.2f %s" result toCurrency
    | None -> printfn "Niepoprawne waluty"

// Zadanie 4
type Account = { AccountNumber: string; Balance: float }
let mutable accounts = Map.empty

let createAccount accNumber =
    accounts <- accounts.Add(accNumber, { AccountNumber = accNumber; Balance = 0.0 })
    printfn "Konto %s utworzone" accNumber

let deposit accNumber amount =
    match accounts.TryFind accNumber with
    | Some acc -> accounts <- accounts.Add(accNumber, { acc with Balance = acc.Balance + amount })
                  printfn "Wpłacono %.2f na konto %s" amount accNumber
    | None -> printfn "Nie znaleziono konta"

let withdraw accNumber amount =
    match accounts.TryFind accNumber with
    | Some acc when acc.Balance >= amount -> accounts <- accounts.Add(accNumber, { acc with Balance = acc.Balance - amount })
    | Some _ -> printfn "Niewystarczające środki"
    | None -> printfn "Nie znaleziono konta"

let checkBalance accNumber =
    match accounts.TryFind accNumber with
    | Some acc -> printfn "Saldo konta %s: %.2f" accNumber acc.Balance
    | None -> printfn "Nie znaleziono konta"

bmiApp()
// currencyConverterApp()
// createAccount "12345"; deposit "12345" 100.0; withdraw "12345" 50.0; checkBalance "12345"
