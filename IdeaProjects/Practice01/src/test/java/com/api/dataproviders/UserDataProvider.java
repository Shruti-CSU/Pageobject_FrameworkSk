package com.api.dataproviders;

import com.api.models.Users;
import org.testng.annotations.DataProvider;

public class UserDataProvider {

    @DataProvider(name = "createUserData")
    public static Object[][] getUsers() {
        return new Object[][]{
                {new Users("John", "John456", "user1@gmail.com"), 201},
                {new Users("emptyname", "", "empty1@gmail.com"), 201},
                {new Users("emptyemail", "Email1", ""),201}
        };
    }
}
