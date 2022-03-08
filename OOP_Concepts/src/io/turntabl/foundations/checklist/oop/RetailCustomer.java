// So here we do not update aby code in the Customer class, we rather include a new property for Corporate customers
// In Ghana, they usually have an officer from the bank who is their point of contact when they need to do something.

public class CorporateCustomer extends Customer {
    public String personalBankerId;        
}