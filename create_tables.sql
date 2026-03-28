-- ============================================
-- Sales Data Pipeline - Schema
-- Database: PostgreSQL
-- ============================================

-- Create products table
CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco NUMERIC(10,2) NOT NULL,
    estoque INT NOT NULL,
    data_cadastro DATE NOT NULL
);

-- Create index for better query performance
CREATE INDEX IF NOT EXISTS idx_produtos_categoria ON produtos(categoria);
CREATE INDEX IF NOT EXISTS idx_produtos_data ON produtos(data_cadastro);

-- Grant permissions (security best practice)
REVOKE ALL ON produtos FROM PUBLIC;
GRANT SELECT, INSERT, UPDATE ON produtos TO bi_user;

-- Add comments for documentation
COMMENT ON TABLE produtos IS 'Product catalog for e-commerce sales analysis';
COMMENT ON COLUMN produtos.preco IS 'Product price in BRL';
COMMENT ON COLUMN produtos.estoque IS 'Current stock quantity';