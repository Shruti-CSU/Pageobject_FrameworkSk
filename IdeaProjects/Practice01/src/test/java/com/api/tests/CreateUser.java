package com.api.tests;

import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

import static io.restassured.RestAssured.given;

public class CreateUser {
    @Test
    public void createuser()  throws Exception {
        // Read JSON payload from file
        String payload = new String(Files.readAllBytes(Paths.get("src/test/resources/payloads/CreateUser.json")));

        Response response = given()
                .header("Content-Type", "text/plain")
                .body(payload)
                .when()
                .post("https://jsonplaceholder.typicode.com/users");

        System.out.println(response.asString());

        // Validate status code
        Assert.assertEquals(response.getStatusCode(), 201);

    }


}
