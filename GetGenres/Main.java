
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by Maria Antoniak on 5/6/2014.
 */


public class Main {
    public static void main(String[] args) {
        String isbnFileName = args[0];
        ArrayList<String> isbnList = getISBNList(isbnFileName);
        for (String isbn : isbnList) {
            getGenres(isbn);
        }
    }

    /**
     * @param isbnFileName text file containing unique ISBN numbers, one per line.
     * @return a list of unique ISBN numbers.
     */
    public static ArrayList<String> getISBNList(String isbnFileName) {
        try {
            ArrayList<String> isbnList = new ArrayList<String>();
            BufferedReader br = new BufferedReader(new FileReader(isbnFileName));
            String line = null;
            while ((line = br.readLine()) != null) {
                isbnList.add(line.trim());
            }
            br.close();
            return isbnList;
        } catch (FileNotFoundException e) {
            System.err.println(e);
            return null;
        } catch (IOException e) {
            System.err.println(e);
            return null;
        }
    }

    /**
     * Scrapes GoodReads.com to get the genres for a given ISBN number.
     * Prints a comma-delimited list of ranked genres, followed by a comma-delimited
     * list of the number of users who voted for each genre.
     * @param isbn a string containing one ISBN number.
     */
    public static void getGenres(String isbn) {
        ArrayList<String> genreList = new ArrayList<String>();
        ArrayList<String> userList = new ArrayList<String>();

        try {
            // Scrape GoodReads using the book's ISBN number (product number in Amazon review corpus).
            Document doc = Jsoup.connect("https://www.goodreads.com/book/isbn/" + isbn).get();

            // Check that the ISBN number leads to a real book page.
            if ((doc.select("div[class=leftContainer exploreBooks]")).size() != 0) {
                return;
            }

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

            // Print genres and numbers of user votes to stdout.
            if (genreList.size() != 0) {
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
                System.out.println();
            }
        }
        catch (IOException e) {
            System.err.println(e);
        }
    }
}