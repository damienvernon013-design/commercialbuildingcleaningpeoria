#!/usr/bin/env python3
"""Generates sitemap.xml and robots.txt from the built pages list."""
import os

BASE_URL = "https://commercialbuildingcleaningpeoria.com"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(OUT_DIR, "_pages_built.txt")) as f:
    paths = sorted(f.read().splitlines())

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in paths:
    sitemap.append(f"  <url><loc>{BASE_URL}{p}</loc></url>")
sitemap.append("</urlset>")

with open(os.path.join(OUT_DIR, "sitemap.xml"), "w") as f:
    f.write("\n".join(sitemap) + "\n")

robots = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
with open(os.path.join(OUT_DIR, "robots.txt"), "w") as f:
    f.write(robots)

print(f"sitemap.xml written with {len(paths)} URLs")
print("robots.txt written")
