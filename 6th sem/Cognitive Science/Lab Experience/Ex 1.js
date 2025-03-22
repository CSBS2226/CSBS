// 1.Basic Arithmetic Operations
var add = 5 + 3;
var subtract = 10 - 6;
var multiply = 4 * 7;
var divide = 20 / 5;
display("Addition (5 + 3): " + add);
display("Subtraction (10 - 6): " + subtract);
display("Multiplication (4 * 7): " + multiply);
display("Division (20 / 5): " + divide);
// 2. Exponentiation
var power = Math.pow(2, 3); // 2^3
display("2 to the power of 3: " + power);
// 3. Square Root
var sqrt = Math.sqrt(16); // √16
display("Square root of 16: " + sqrt);
// 4. Trigonometric Functions
var sinVal = Math.sin(Math.PI / 2); // Sin(90 degrees)
var cosVal = Math.cos(0); // Cos(0 degrees)
display("Sin(90 degrees): " + sinVal);
display("Cos(0 degrees): " + cosVal);
// 5. Logarithm
var logVal = Math.log(10); // Natural log of 10
display("Natural Log of 10: " + logVal);
// 6. Random Numbers
var randomNumber = Math.random(); // Random number between 0 and 1
display("Random Number: " + randomNumber);
// 7. Probability Distribution Example
var flipCoin = flip(0.5); // Simulates a fair coin toss
display("Coin Flip Result (1 = Heads, 0 = Tails): " + flipCoin)
