package com.codewars.katas.collections;

public class ExtractFileName {

	public static void main(String[] args) {
		
		System.out.println(extractFileName("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"));
		System.out.println(extractFileName("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"));
	}
	
	public static String extractFileName(String dirtyFileName) {
		return dirtyFileName.substring(dirtyFileName.indexOf("_") + 1, dirtyFileName.lastIndexOf("."));
	}

}
