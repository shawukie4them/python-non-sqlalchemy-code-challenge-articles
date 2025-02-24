#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    author1 = Author("James Bond")
    author2 = Author("Jane Bond")

    magazine1 = Magazine("Tech Weekly", "Technology")
    magazine2 = Magazine("Fashion Forward", "Fashion")

    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author1, magazine2, "Fashion Trends 2025")
    article2 = Article(author2, magazine1, "Cybersecurity in 2024")

    print("\nTesting Methods:")
    print(f"{author1.name}'s Articles: {[article.title for article in author1.articles()]}")
    print(f"{author1.name}'s Magazines: {[mag.name for mag in author1.magazines()]}")
    print(f"{magazine1.name}'s Articles: {[article.title for article in magazine1.articles()]}")
    print(f"{author1.name}'s Contributors: {[contributor.name for contributor in magazine1.contributors()]}")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
