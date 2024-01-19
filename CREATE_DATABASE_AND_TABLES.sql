CREATE TABLE public.categorias (
    id_categoria integer NOT NULL,
    nome_categoria character varying(100) NOT NULL,
    CONSTRAINT categorias_pkey PRIMARY KEY (id_categoria)
);

CRATE TABLE public.livros (
    id_livro integer NOT NULL,
    titulo_livro character varying(100) NOT NULL,
    codigo_barra character varying(100) NOT NULL,
    id_categoria integer NOT NULL,
    preco real NOT NULL,
    quantidade_estoque integer,
    avaliacao integer,
    CONSTRAINT livros_pkey PRIMARY KEY (id_livro),
    CONSTRAINT livros_id_categoria_fkey FOREIGN KEY (id_categoria)
        REFERENCES public.categorias (id_categoria) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
