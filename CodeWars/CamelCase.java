package com.codewars.katas.collections;

public class CamelCase {

	public static void main(String[] args) {
        System.out.println(camelCase("test case"));
        System.out.println(camelCase("camel case method"));
        System.out.println(camelCase(" camel case word"));
        System.out.println(camelCase("say hello "));

	}
	
	public static String camelCase(String str) {
		
		if(str == null || str.length() == 0) {
			return "";
		}
		
		String[] words = str.trim().split(" +");
		String result = "";
		
		for(int i=0; i<words.length; i++) {
			result += words[i].substring(0, 1).toUpperCase();
			result += words[i].substring(1, words[i].length()).toLowerCase();
		}
		
		return result;
		
	}
	


}
