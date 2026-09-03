# biblioteca_bdd - Aplicação com Banco de Dados

Implementação do exemplo clássico da Biblioteca em um banco de dados *sqlite*.

As tabelas do projeto são:

**usuarios**(*id, nome*)  
**autores**(*id, nome*)  
**livros**(*id, titulo, autor_id, ano_publicacao, edicao, disponivel*)  
**emprestimos**(*id, usuario_id, data*)  
**emprestimos**(*id, usuario_id*)  
**emprestimos_id**(*emprestimos_id, livro_id, data_devolucao*)   