import io.restassured.RestAssured;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.specification.ResponseSpecification;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static io.restassured.RestAssured.given;

public class AccountTests {
    static Map<String, String> headers = new HashMap<>();

    ResponseSpecification responseSpecification = null;

    @BeforeAll
    static void setUp() {
        headers.put("Authorization", "Client-ID 63679dfca8eb551");
        RestAssured.requestSpecification = null;
    }

    @BeforeEach
    void beforeTest() {
        responseSpecification = new ResponseSpecBuilder()
                .expectStatusCode(200)
                .expectStatusLine("HTTP/1.1 200 OK")
                .expectContentType(ContentType.JSON)
                .expectResponseTime(Matchers.lessThan(5000L))
                .expectHeader("Access-Control-Allow-Credentials", "true")
                .build();
    }

    @Test
    void getAccountInfoTest1() {
        given()
                .headers(headers)
                .when()
                .get("https://api.imgur.com/3/account/romik0")
                .then()
                .statusCode(200)
                .contentType("application/json")
                .extract()
                .response()
                .jsonPath();
            }

    @Test
    void getAccountInfoTest2() {
        given()
                .headers(headers)
                .when()
                .get("https://api.imgur.com/3/account/romik0")
                .prettyPeek()
                .then()
                //changed to assertion with responseSpec
                .spec(responseSpecification);
    }

    @Test
    void getAllImages() {
        String[] names = {"Ki6DoeS", "LsB6eMt", "VlxeQ8c","P8i0Fu8", "NCDrNqS", "S9EEOIR", "C6xJJZO","wVg94iX", "P8e1sUc"};
        for(String name: names) {
            given()
                    .headers(headers)
                    .when()
                    .get("https://api.imgur.com/3/image/" + name)
                    .then()
                    .statusCode(200)
                    .contentType("application/json")
                    .extract()
                    .response()
                    .jsonPath();
        }
    }
}

