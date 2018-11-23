package com.example.helly_jainee.publicparking;

public class Item {
    public String text;
    public String color;

    public Item(String text, String color ) {
        this.text = text;
        this.color = color;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}
