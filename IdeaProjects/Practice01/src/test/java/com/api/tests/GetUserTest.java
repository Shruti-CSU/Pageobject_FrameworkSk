package com.api.tests;

import com.api.base.BaseTest;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;

public class GetUserTest extends BaseTest {
    @Test
    public void getUserByID () {

        Response response = given()
                .when()
                .get("https://jsonplaceholder.typicode.com/users");

        System.out.println(response.asString());

        //Validate Status code
        Assert.assertEquals(response.getStatusCode(), 200);

        // Validate some response value
        int userId = response.jsonPath().getInt("[0].id");
        System.out.println("First user ID:" + userId);
    }

}
