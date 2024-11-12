Data Science Capstone - Module 1
================
November 12, 2024

## en_US.blogs.txt file is how many megabytes

``` r
# Get the file size in bytes
file_size_bytes <- file.info("data/en_US/en_US.blogs.txt")$size

# Convert bytes to megabytes (MB)
file_size_mb <- file_size_bytes / (1024 * 1024)

# Print the file size in MB
print(paste("File size:", round(file_size_mb, 2), "MB"))
```

    ## [1] "File size: 200.42 MB"

## en_US.twitter.txt has how many lines of text?

``` r
# Read the file into a character vector, each element representing a line
twitter_lines <- readLines("data/en_US/en_US.twitter.txt")
```

    ## Warning in readLines("data/en_US/en_US.twitter.txt"): line 167155 appears to
    ## contain an embedded nul

    ## Warning in readLines("data/en_US/en_US.twitter.txt"): line 268547 appears to
    ## contain an embedded nul

    ## Warning in readLines("data/en_US/en_US.twitter.txt"): line 1274086 appears to
    ## contain an embedded nul

    ## Warning in readLines("data/en_US/en_US.twitter.txt"): line 1759032 appears to
    ## contain an embedded nul

``` r
# Count the number of elements in the vector
num_lines <- length(twitter_lines)

print(paste("Number of lines in en_US.twitter.txt:", num_lines))
```

    ## [1] "Number of lines in en_US.twitter.txt: 2360148"

## What is the length of the longest line seen in any of the three en_US data sets?

``` r
library(tidyverse)
```

    ## Warning: package 'tidyverse' was built under R version 4.3.3

    ## Warning: package 'ggplot2' was built under R version 4.3.3

    ## Warning: package 'tibble' was built under R version 4.3.3

    ## Warning: package 'tidyr' was built under R version 4.3.3

    ## Warning: package 'readr' was built under R version 4.3.3

    ## Warning: package 'purrr' was built under R version 4.3.3

    ## Warning: package 'dplyr' was built under R version 4.3.3

    ## Warning: package 'forcats' was built under R version 4.3.3

    ## Warning: package 'lubridate' was built under R version 4.3.3

    ## ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
    ## ✔ dplyr     1.1.4     ✔ readr     2.1.5
    ## ✔ forcats   1.0.0     ✔ stringr   1.5.1
    ## ✔ ggplot2   3.5.0     ✔ tibble    3.2.1
    ## ✔ lubridate 1.9.3     ✔ tidyr     1.3.1
    ## ✔ purrr     1.0.2     
    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()
    ## ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

``` r
# Function to get the longest line in a file
get_longest_line <- function(file_path) {
  read_lines(file_path) %>% 
    str_length() %>% 
    max()
}

# Get the longest line length for each file
blogs_length <- get_longest_line("data/en_US/en_US.blogs.txt")
news_length <- get_longest_line("data/en_US/en_US.news.txt")
twitter_length <- get_longest_line("data/en_US/en_US.twitter.txt")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

``` r
# Find the maximum length and corresponding file
max_length <- max(blogs_length, news_length, twitter_length)
max_file <- ifelse(max_length == blogs_length, "en_US.blogs.txt",
                   ifelse(max_length == news_length, "en_US.news.txt", "en_US.twitter.txt"))

print(paste("The longest line is", max_length, "characters long and is found in", max_file))
```

    ## [1] "The longest line is 40833 characters long and is found in en_US.blogs.txt"

## In the en_US twitter data set, if you divide the number of lines where the word “love” (all lowercase) occurs by the number of lines the word “hate” (all lowercase) occurs, about what do you get?

``` r
library(tidyverse)

# Read the twitter data
twitter_data <- read_lines("data/en_US/en_US.twitter.txt")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

``` r
# Count the occurrences of "love" and "hate"
love_count <- sum(str_detect(twitter_data, "\\blove\\b"))
hate_count <- sum(str_detect(twitter_data, "\\bhate\\b"))

# Calculate the ratio
love_hate_ratio <- love_count / hate_count

print(paste("The ratio of 'love' to 'hate' in the Twitter data is approximately:", round(love_hate_ratio, 2)))
```

    ## [1] "The ratio of 'love' to 'hate' in the Twitter data is approximately: 4.99"

## The one tweet in the en_US twitter data set that matches the word “biostats” says what?

``` r
library(tidyverse)

# Read the twitter data
twitter_data <- read_lines("data/en_US/en_US.twitter.txt")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

``` r
# Find the tweet containing "biostats"
biostats_tweet <- twitter_data[str_detect(twitter_data, "\\bbiostats\\b")]

print(biostats_tweet)
```

    ## [1] "i know how you feel.. i have biostats on tuesday and i have yet to study =/"

# 

``` r
library(tidyverse)

# Read the twitter data
twitter_data <- read_lines("data/en_US/en_US.twitter.txt")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

``` r
# Count the exact matches
exact_match_count <- sum(twitter_data == "A computer once beat me at chess, but it was no match for me at kickboxing")

print(paste("Number of exact matches:", exact_match_count))
```

    ## [1] "Number of exact matches: 3"
