package com.api.tests;

import com.api.base.BaseTest;
import com.api.constants.EndPoints;
import com.api.dataproviders.UserDataProvider;
import com.api.models.Users;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.nio.file.Files;
import java.nio.file.Paths;

import static io.restassured.RestAssured.given;

public class CreateUserTest  extends BaseTest {

    @Test(dataProvider = "createUserData", dataProviderClass = UserDataProvider.class)
    public void createUserTest(Users user, int expectedStatus) {

        Response response = given()
                .header("Content-Type", "application/json")
                .body(user)
                .when()
                .post(EndPoints.CREATE_USER);

        Assert.assertEquals(response.getStatusCode(), expectedStatus);
    }
}
