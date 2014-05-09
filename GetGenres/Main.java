
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * Created by Maria Antoniak on 5/6/2014.
 */


public class Main {
    public static void main(String[] args) throws IOException {

        ArrayList<String> genreList = new ArrayList<String>();
        ArrayList<String> userList = new ArrayList<String>();

        // Scrape GoodReads using the book's ISBN number (product number in Amazon review corpus).
        String isbn = "1550742884";
        Document doc = Jsoup.connect("https://www.goodreads.com/book/isbn/" + isbn).get();

        // Get ranked list of genres.
        Elements links = doc.select("div[class=left]");
        for (Element link : links) {
            Elements genres = link.select("a[href^=/genres/]");
            String genreString = "";
            for (int i = 0; i < genres.size(); i++) {
                genreString += genres.get(i).text();
                if ((genres.size() > 1) && (i != (genres.size() - 1))) {
                    genreString += ("/");
                }
            }
            genreList.add(genreString);
        }

        // Get number of users who voted for each genre.
        links = doc.select("div[class=right]");
        for (Element link : links) {
            Elements users = link.select("a[href^=/shelf/users/]");
            for (Element user : users) {
                userList.add(user.text());
            }
        }

        // Print results to stdout (user friendly).
//        for (int i = 0; i < genreList.size(); i++) {
//            System.out.print(genreList.get(i) + " (" + userList.get(i) + ")");
//            if (i != (genreList.size() - 1)) {
//                System.out.print(", ");
//            }
//        }

        // Print results to stdout.
        System.out.println(isbn);
        for (int i = 0; i < genreList.size(); i++) {
            System.out.print(genreList.get(i));
            if (i != (genreList.size() - 1)) {
                System.out.print(", ");
            }
        }
        System.out.println();
        for (int i = 0; i < userList.size(); i++) {
            System.out.print(userList.get(i).split(" ")[0]);
            if (i != (userList.size() - 1)) {
                System.out.print(", ");
            }
        }
    }
}