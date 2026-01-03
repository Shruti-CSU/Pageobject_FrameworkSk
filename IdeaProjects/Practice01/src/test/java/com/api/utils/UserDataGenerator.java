package com.api.utils;

import com.api.models.Users;

import java.util.ArrayList;
import java.util.List;

public class UserDataGenerator {

    public static List<Users> generateUsers(int count) {
        List<Users> users = new ArrayList<>();

        for (int i = 1; i <= count; i++) {
            users.add(new Users(
                    "User" + i,
                    "Username" + i,
                    "email" + i + "@test.com"
            ));
        }
        return users;
    }
}
