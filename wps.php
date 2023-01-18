<?php

// Function to check if a website is using WordPress
function check_wordpress($url) {
    $login_url = $url . '/wp-login.php';
    $response = @file_get_contents($login_url);
    if ($response !== false) {
        return true;
    } else {
        return false;
    }
}

// Function to enumerate WordPress plugins
function enumerate_plugins($url) {
    $plugins_url = $url . '/wp-content/plugins/';
    $response = @file_get_contents($plugins_url);
    if ($response !== false) {
        preg_match_all('/<a href="(.*?)">/', $response, $matches);
        return $matches[1];
    } else {
        return array();
    }
}

// Function to check if a plugin is vulnerable
function check_vulnerability($plugin) {
    $vuln_db_url = "https://wpvulndb.com/vulnerabilities/" . $plugin;
    $response = @file_get_contents($vuln_db_url);
    if (strpos($response, "No vulnerabilities found")) {
        return false;
    } else {
        return true;
    }
}

// Example usage
if(isset($_POST['submit'])){
  $url = $_POST['url'];
  if (check_wordpress($url)) {
      echo "<h1>Website is using WordPress.</h1>";
      $plugins = enumerate_plugins($url);
      if (count($plugins) > 0) {
          echo "<h2>Enumerated plugins:</h2>";
          echo "<ul>";
          foreach ($plugins as $plugin) {
              if (check_vulnerability($plugin)) {
                  echo "<li>" . $plugin . " is <b style='color:red'>vulnerable</b></li>";
              } else {
                  echo "<li>" . $plugin . " is <b style='color:green'>not vulnerable</b></li>";
              }
          }
          echo "</ul>";
      } else {
          echo "<h2>Failed to enumerate plugins.</h2>";
      }
  } else {
      echo "<h1>Website is not using WordPress.</h1>";
  }
}
else{
  echo '
  <form action="'.$_SERVER['PHP_SELF'].'" method="post">
    <label for="url">Website URL</label>
    <input type="text" id="url" name="url">
    <input type="submit" value="Submit" name="submit">
  </form>
  ';
