public interface Customer {
    void collectMoney(String bankOfficialID);

    void getCustomerDetails();
}

class RetailCustomer implements Customer {
    @Override
    public void collectMoney(String bankOfficialID) {
        // ....
    }

    @Override 
    public void getCustomerDetails(){
        return "Mary Jonah, and I live in Ghana";
    }
}

class CorporateCustomer implements Customer {
    @Override
    public void collectMoney(String bankOfficialID) {
        return bankOfficialID + " comes for the money on Mondays."
    }

    @Override 
    public void getCustomerDetails(){
        return "Candle International Company located in Accra, Ghana.";
    }
}

// RetailCustomer is forced to implement the method collectMoney and it does not need it
    // Rather create another interface: Collectable and have getCustomerDetails stand alone in Customer interface

interface Collectable {
    void collectMoney(String bankOfficialID);
}