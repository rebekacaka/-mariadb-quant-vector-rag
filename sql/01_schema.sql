-- One row per Wikipedia article (the "parent").
CREATE TABLE articles (
  article_id  INT PRIMARY KEY AUTO_INCREMENT,
  title       VARCHAR(255) NOT NULL,
  category    VARCHAR(64),
  url         VARCHAR(512) NOT NULL
);

-- Many rows per article (the "children"): a short passage plus its embedding.
CREATE TABLE chunks (
  chunk_id    INT PRIMARY KEY AUTO_INCREMENT,
  article_id  INT NOT NULL,
  chunk_text  TEXT NOT NULL,
  embedding   VECTOR(384) NOT NULL,
  FOREIGN KEY (article_id) REFERENCES articles(article_id) ON DELETE CASCADE
);
