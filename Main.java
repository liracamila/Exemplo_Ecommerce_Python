import java.util.ArrayList;
import java.util.Scanner;

class Produto {
    private String nome;
    private double preço;
    private int quantidade;

    public Produto(String nome, double preço, int quantidade) {
        this.nome = nome;
        this.preço = preço;
        this.quantidade = quantidade;
    }

    public String getNome () {
        return nome;}
    public void setNome(String nome) {
        this.nome = nome;}

    public double getPreço () {
        return preço;}
    public void setPreço(double preço) {
        this.preço = preço;}

    public int getQuantidade () {
        return quantidade;}
    public void etQuantidade(int quantidade) {
        this.quantidade = quantidade;}

    @Override
    public String toString () {
        return "Nome: " + nome + ", Preço: R$ " + preço + " , Quantidade: " + quantidade;
    }

}

class CadastroDeProduto {
    private ArrayList<Produto> listaProdutos = new ArrayList<>();

    public void CadastrarProduto(Produto produto){
        listaProdutos.add(produto);
        System.out.println("Produto cadastrado com sucesso!");
    }

    public void VisualizarProdutos(){
        if (listaProdutos.isEmpty()){
            System.out.println("Nenhum produto cadastrado.");
        } else {
            System.out.println("Lista de Produtos: ");
                for (Produto produto : listaProdutos){
                    System.out.println(produto.toString());
                }
        }
    }

    public void filtrarPreco(double precoMin, double precoMax){
        ArrayList<Produto> produtosFiltrados = new ArrayList<>();
        for (Produto produto: listaProdutos){
            if (produto.getPreço() >= precoMin && produto.getPreço() <= precoMax){
                produtosFiltrados.add(produto);}
            }
            if (produtosFiltrados.isEmpty()) {
                System.out.println("Nenhum produto encontrado nesta faixa de preço.");
            }
            else{
                System.out.println("Produtos encontrados:");
                for (Produto produto : produtosFiltrados){
                    System.out.println(produto.toString());}
            }
        }
    }

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        CadastroDeProduto cadastroDeProduto = new CadastroDeProduto();
        while(true){
            System.out.println("Escolha uma opção:");
            System.out.println("1- Cadastrar produto");
            System.out.println("2- Vizualizar produtos");
            System.out.println("3- Filtrar produtos por preço");
            System.out.println("0- Sair.");

            int opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("Digite o nome do produto: ");
                    String nome = scanner.next();
                    System.out.println("Digite o preço do produto: R$ ");
                    double preço = scanner.nextDouble();
                    System.out.println("Digite a quantidade: ");
                    int quantidade = scanner.nextInt();
                    Produto produto = new Produto(nome, preço, quantidade);
                    cadastroDeProduto.CadastrarProduto(produto);
                    break;

                case 2:
                    cadastroDeProduto.VisualizarProdutos();
                    break;

                case 3:
                    System.out.println("Digite o preço minimo: R$ ");
                    double precoMin = scanner.nextDouble();
                    System.out.println("Digite o preço maximo: R$ ");
                    double precoMax = scanner.nextDouble();
                    cadastroDeProduto.filtrarPreco(precoMin, precoMax);
                    break;

                case 0:
                    System.out.println("Encerrando o programa.");
                    System.exit(0);
                    break;
            }
        }

    }
}
