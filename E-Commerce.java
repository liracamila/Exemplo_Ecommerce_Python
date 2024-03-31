import java.util.ArrayList;
import java.util.Scanner;

class Produto {
    private String nome;
    private double preço;
    private int quantidade;

    Public Produto(String nome, double preço, int quantidade) {
        this.nome = nome;
        this.preço = preço;
        this.quantidade = quantidade
    }

    Public String getNome () {
        return nome;}
    Public void setNome(String nome) {
        this.nome = nome;}

    Public double getPreço () {
        return preço;}
    Public void setPreço(double preço) {
        this.preço = preço;}

    Public int getQuantidade () {
        return quantidade;}
    Public void etQuantidade(int quantidade) {
        this.quantidade = quantidade;}

    @Override
    public String toString () {
        return "Nome: " + nome ", Preço: R$ " + preço " , Quantidade: " + quantidade;
    }

}
