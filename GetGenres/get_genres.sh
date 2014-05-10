#!/bin/sh
javac -classpath jsoup-1.7.3.jar:. Main.java
java -classpath jsoup-1.7.3.jar:. Main $1 >$2