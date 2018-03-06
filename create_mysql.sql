CREATE TABLE Wholesaler(
    WholesalerID BIGINT NOT NULL AUTO_INCREMENT,
    Website VARCHAR(255),
    WholesalerName VARCHAR(255),
    WholesalerPhone VARCHAR(255),
    WholesalerLocation VARCHAR(255),
    PRIMARY KEY (WholesalerID)
);
CREATE TABLE Staff(
    StaffID BIGINT NOT NULL AUTO_INCREMENT,
    StaffName VARCHAR(255),
    Email VARCHAR(255),
    Wage INT,
    sPassword VARCHAR(255),
    PRIMARY KEY (StaffID)
);
CREATE TABLE Address (
    AddressID BIGINT NOT NULL AUTO_INCREMENT,
    Street VARCHAR(255),
    City VARCHAR(255),
    aState VARCHAR(255),
    Zip VARCHAR(255),
    PRIMARY KEY (AddressID)
);
CREATE TABLE BillingInformation (
    BillingInformationID BIGINT NOT NULL AUTO_INCREMENT,
    CreditCardNumber Int,
    ExpirationDate Date,
    AddressID BIGINT,
    PRIMARY KEY (BillingInformationID),
    FOREIGN KEY (AddressID) REFERENCES Address(AddressID)
);
CREATE TABLE Customer (
    CustomerID BIGINT NOT NULL AUTO_INCREMENT,
    Email VARCHAR(255),
    cName VARCHAR(255),
    Pass VARCHAR(255),
    AddressID BIGINT,
    BillingInformationID BIGINT,
    PRIMARY KEY (CustomerID),
    FOREIGN KEY (AddressID) REFERENCES Address(AddressID),
    FOREIGN KEY (BillingInformationID) REFERENCES BillingInformation(BillingInformationID)
);
CREATE TABLE Cart (
    CartID BIGINT NOT NULL AUTO_INCREMENT,
    NumberOfItems INT,
    TotalCost FLOAT,
    ShippingCost FLOAT,
    CustomerID BIGINT,
    PRIMARY KEY (CartID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE Product(
    ProductID BIGINT NOT NULL AUTO_INCREMENT,
    ShippingCost FLOAT,
    ProductName VARCHAR(255),
    Color VARCHAR(255),
    Price Float,
    WholesalerID BIGINT,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (WholesalerID) REFERENCES Wholesaler(WholesalerID)
);
CREATE TABLE CartedProduct(
    CartedProductID BIGINT NOT NULL AUTO_INCREMENT,
    ProductID BIGINT,
    CartID BIGINT,
    PRIMARY KEY (CartedProductID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (CartID) REFERENCES Cart(CartID)
);

CREATE TABLE NewOrder(
    NewOrderID BIGINT NOT NULL AUTO_INCREMENT,
    CartID BIGINT,
    StaffID BIGINT,
    OrderDate Date,
    PRIMARY KEY (NewOrderID),
    FOREIGN KEY (CartID) REFERENCES Cart(CartID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);