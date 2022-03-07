package io.turntabl.foundations.checklist.oop;

// Single Responsibility Principle
    // Instead the class is separated into individual classes: Customer, Account, and the Bank itself
public class Bank {
    private String customerFirstName;
    private String customerLastName;
    private int customerAccNo;
    private String customerAddress;
    private float accountBalance;
}


class Customer {
    private String customerFirstName;
    private String customerLastName;
    private String customerAddress;
}

class Account {
    private int customerAccNo;
    private float accountBalance;
}

class Bank2 {
    private String bankBranch;
}