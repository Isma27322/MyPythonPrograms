$choices = @("rock", "paper", "scissors", "lizard", "spock")

function Get-UserChoice {
    $userChoice = Read-Host "Enter your choice (Rock, Paper, Scissors, Lizard, Spock)"
    return $userChoice.ToLower()
}

function Get-ComputerChoice {
    $randomIndex = Get-Random -Minimum 0 -Maximum $choices.Count
    return $choices[$randomIndex]
}

function Winner {
    param(
        [string]$userChoice,
        [string]$computerChoice
    )

    Write-Host "You chose $userChoice"
    Write-Host "Computer chose $computerChoice"

    if ($userChoice -eq $computerChoice) {
        Write-Host "It's a tie!"
    } elseif (
        ($userChoice -eq "rock" -and ($computerChoice -eq "scissors" -or $computerChoice -eq "lizard")) -or
        ($userChoice -eq "paper" -and ($computerChoice -eq "rock" -or $computerChoice -eq "spock")) -or
        ($userChoice -eq "scissors" -and ($computerChoice -eq "paper" -or $computerChoice -eq "lizard")) -or
        ($userChoice -eq "lizard" -and ($computerChoice -eq "spock" -or $computerChoice -eq "paper")) -or
        ($userChoice -eq "spock" -and ($computerChoice -eq "scissors" -or $computerChoice -eq "rock"))
    ) {
        Write-Host "You win!"
    } else {
        Write-Host "Computer wins!"
    }
}

$userChoice = Get-UserChoice
$computerChoice = Get-ComputerChoice
Winner -userChoice $userChoice -computerChoice $computerChoice
