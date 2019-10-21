# Django Fun Times
---
### Prerequisites and setup
Getting started:
```
git clone https://github.com/notmarkmiranda/django_fun_times.git
cd django_fun_times
```

In order to run this application, you will need Python3 installed. You can use Homebrew to install it with:
```
brew install python3
```

You can verify Python3 with:
```
python3 -V
=> Python 3.7.4
```

After you have installed and/or verified your installation, you can get the application running with:
```
./vamonos.sh
```

Then pop open your favorite browser and navigate to `http://localhost:8000`

---
General
---
### Future Additions
- Series Index page to allow users to filter down by article series
- Filler information for stock quotes without images or unknown markets.
- Author show page for bios (social media links) and all articles written by author.

## Improvement
- This is the first time I've built a project in Django and I don't know a lot of the conventions or design paradigms
- Add jQuery to clean up some of the vanilla JS I wrote.

## Optimization
- Implement memoization or caching to prevent the main(articles#index) page from querying the Content API on refresh
- Implement memoization or caching to prevent the article(articles#show) page from querying the Quotes API on refresh