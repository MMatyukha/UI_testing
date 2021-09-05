import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static io.restassured.RestAssured.given;

public class AccountTests {
    static Map<String, String> headers = new HashMap<>();

    @BeforeAll
    static void setUp() {
        headers.put("Authorization", "Client-ID 63679dfca8eb551");
    }
 
    @Test
    void getAccountInfoTest() {
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
            
}