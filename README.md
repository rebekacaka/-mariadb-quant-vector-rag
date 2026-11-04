A project for area 4, "Vector search and RAG, natively" for the [MariaDB student database projects, 2026-09](https://mariadb.org/bachelor_hackathon_2026-09/).

# QuantRAG: semantic search for quantitative finance, inside MariaDB

A study companion for quantitative finance. A student types a question in their own words and the
system finds the right passage in a Wikipedia corpus of finance and economics articles, using
MariaDB's native `VECTOR` type and `VECTOR INDEX`. Finance language is full of near-synonyms and
double meanings (VaR vs expected shortfall, implied vs realised volatility, "swap", "margin"), so
the project also measures where this kind of search gets confused, and which fixes help.

**Status:** work in progress. The database schema and Docker setup exist; ingestion, search and
measurements are being built.

Developed against **MariaDB 11.8.9** (Docker image `mariadb:11.8`).

## Quick start (current state)

```bash
cp .env.example .env        # then edit .env and choose your own password
docker compose up -d --wait
docker compose exec -T db sh -c 'mariadb -uroot -p"$MARIADB_ROOT_PASSWORD" quantrag' < sql/01_schema.sql
```

## Team

To be completed.
