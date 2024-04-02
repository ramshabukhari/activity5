# activity5

## Prompt: Refactoring Monolithic Python Code

## Introduction:
In this exercise, you'll have the opportunity to work with a monolithic Python codebase and practice refactoring it into more modular, maintainable components. The goal is to improve readability, reusability, and overall code quality.

## Step 1: Understand Monolithic Code

Given to you is a monolithic Python script that simulates a simple banking system. The script allows users to create accounts, deposit and withdraw funds, and view their account balances. Additionally, it has basic error handling to manage cases such as insufficient funds or invalid input.

## Step 2: Refactor the Monolithic Code

Review the monolithic code and identify areas where the code can be refactored for better organization and readability.
Break down the code into smaller, more focused functions or classes, each responsible for a specific aspect of the banking system.
Apply appropriate design principles such as separation of concerns, single responsibility principle, and DRY (Don't Repeat Yourself) principle.
Aim to create reusable components that can be easily maintained and tested independently.

## Example Refactoring:

Separate the functionality for account creation, deposit, withdrawal, and balance viewing into distinct functions or methods.
Encapsulate related functionality into classes, such as an Account class for managing individual accounts and a Bank class for overall bank operations.
Implement error handling to handle cases like insufficient funds, invalid input, or account not found.
Utilize logging to track transactions and errors for auditing and debugging purposes.

## Step 3: Test and Validate

Test the refactored code through unit testing to ensure that it produces the same results as the original monolithic version.
Verify that the refactored code is more modular, easier to understand, and maintain.

## Conclusion:

Reflect on the process of refactoring the monolithic code and the benefits gained from modularization. Consider how breaking down the code into smaller components improves readability, reusability, and maintainability. 

Submit the refactored code through the same repo.
