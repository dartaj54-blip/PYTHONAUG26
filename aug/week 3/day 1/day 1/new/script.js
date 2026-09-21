// 1. Student Marks

let m1 = 80;
let m2 = 75;
let m3 = 90;
let m4 = 85;
let m5 = 70;

let total = m1 + m2 + m3 + m4 + m5;
let percentage = total / 5;

console.log("Total Marks:", total);
console.log("Percentage:", percentage + "%");


// 2. Product Discount

let price = 1200;
let discount = 15;

let discountAmount = price * discount / 100;
let finalPrice = price - discountAmount;

console.log("Discount Amount:", discountAmount);
console.log("Final Price:", finalPrice);


// 3. Square and Cube

let num = 5;

let square = num * num;
let cube = num * num * num;

console.log("Square:", square);
console.log("Cube:", cube);


// 4. Positive, Negative or Zero

let number = -10;

if (number > 0) {
    console.log("Positive");
} else if (number < 0) {
    console.log("Negative");
} else {
    console.log("Zero");
}


// 5. Student Grade

let marks = 85;

if (marks >= 90 && marks <= 100) {
    console.log("Grade A");
} else if (marks >= 80) {
    console.log("Grade B");
} else if (marks >= 70) {
    console.log("Grade C");
} else if (marks >= 60) {
    console.log("Grade D");
} else {
    console.log("Fail");
}


// 6. Even or Odd

let n = 8;

if (n % 2 == 0) {
    console.log("Even");
} else {
    console.log("Odd");
}


// 7. Largest of Three Numbers

let a = 20;
let b = 35;
let c = 15;

if (a > b && a > c) {
    console.log("Largest Number:", a);
} else if (b > a && b > c) {
    console.log("Largest Number:", b);
} else {
    console.log("Largest Number:", c);
}


// 8. Pattern

for (let i = 1; i <= 5; i++) {

    let line = "";

    for (let j = 1; j <= i; j++) {
        line = line + j;
    }

    console.log(line);
}


// 9. Count Numbers Divisible by 3 and 5

let count = 0;

for (let i = 1; i <= 100; i++) {

    if (i % 3 == 0 && i % 5 == 0) {
        count++;
    }

}

console.log("Count:", count);


// 10. Factorial

let factNum = 5;
let factorial = 1;

for (let i = 1; i <= factNum; i++) {
    factorial = factorial * i;
}

console.log("Factorial:", factorial);


// 11. Multiplication Table Function

function multiplicationTable(num) {

    for (let i = 1; i <= 10; i++) {
        console.log(num + " x " + i + " = " + num * i);
    }

}

multiplicationTable(5);


// 12. Sum Function

function add(a, b) {

    return a + b;

}

let result = add(10, 20);

console.log("Sum:", result);


// 13. ATM Simulation

let balance = 10000;

function deposit(amount) {

    balance = balance + amount;

    console.log("Deposited:", amount);
    console.log("Balance:", balance);

}

function withdraw(amount) {

    if (amount <= balance) {

        balance = balance - amount;

        console.log("Withdraw:", amount);
        console.log("Balance:", balance);

    } else {

        console.log("Insufficient Balance");

    }

}

function checkBalance() {

    console.log("Current Balance:", balance);

}

deposit(2000);

withdraw(3000);

checkBalance();