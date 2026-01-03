package com.api.models;

public class Users {

    private String name;
    private String username;
    private String email;

    // Constructor
    public Users(String name, String username, String email) {
        this.name = name;
        this.username = username;
        this.email = email;
    }

    // Getters and setters (optional, REST Assured can serialize fields directly)
    // Getters stand for GetAPI like GET and setters stand for SetAPI like POST
    public String getName() {
        return name;
    }
    public void setName(String name) {this.name = name;}
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {this.username = username;}
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {this.email = email;}
}
