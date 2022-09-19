import java.util.Arrays;

public class MergeSort
{
	private static final int n = 100;	// Tamanho do vetor
	static int menorValor;
	static int indiceMenorValor;
	static int qntTrocas;
	static int qntComparacoes;

	public static void main(String[] args)
	{
	
		int [] vetorAleatorio = CriaVetorAleatorio(n);
		Sort(vetorAleatorio);
		System.out.println("\nORDENAÇÃO COM NÚMEROS ALEATÓRIOS: \n");
		System.out.println(Arrays.toString(vetorAleatorio));
		System.out.println("\nNúmero de trocas: " + qntTrocas);
		System.out.println("\nNúmero de comparações: "+ qntComparacoes);
		System.out.println("\n----------------------------------------\n");
		
		int [] vetorCrescente = CriaVetorCrescente(n);
		Sort(vetorCrescente);
		System.out.println("ORDENAÇÃO COM NÚMEROS CRSCENTES: \n");
		System.out.println(Arrays.toString(vetorCrescente));
		System.out.println("\nNúmero de trocas: " + qntTrocas);
		System.out.println("\nNúmero de comparações: " + qntComparacoes);
		System.out.println("\n----------------------------------------\n");
		
		int [] vetorDecrescente = CriaVetorDecrescente(n);
		Sort(vetorDecrescente);
		System.out.println("ORDENAÇÃO COM NÚMEROS DECRESCENTES: \n");
		System.out.println(Arrays.toString(vetorDecrescente));
		System.out.println("\nNúmero de trocas: " + qntTrocas);
		System.out.println("\nNúmero de comparações: " + qntComparacoes);
		
		
	}
	
	private static void Sort(int[] vetor)
	{
		for(int i = 0; i < vetor.length -1; i++)
	    {
	        // antes de comparar, considera-se o menor valor, o valor atual do loop.

	        menorValor = vetor[i];
	        indiceMenorValor = i;

	         // compara com os outros valores do vetor

	         for(int j = i + 1;j < vetor.length; j++)
	         {
	           if(vetor[j] < menorValor)
	           {
	             menorValor = vetor[j];
	             indiceMenorValor = j;
	             
	             qntTrocas = i + 1;
	           }
	           
	           qntComparacoes++;
	           
	         }

	      // Troca os valores menor e maior:

	      vetor[indiceMenorValor] = vetor[i];
	      vetor[i] = menorValor;
	      
	    }
	}

	public static int[] CriaVetorAleatorio(int n)
	{
		qntTrocas = 0;
		qntComparacoes = 0; 
		
		int [] vetor = new int[n];
		
		for(int i = 0; i < vetor.length; i++)
		{
			int rnd = (int) (1 + Math.random() * 100);
			vetor[i] = rnd;
		}
		
		return vetor; 
	}

	public static int[] CriaVetorCrescente(int n)
	{
		qntTrocas = 0;
		qntComparacoes = 0; 
		
		int [] vetor = new int[n];
		
		for(int i = 0; i < n; i++)
		{
			vetor[i] = i;
		}
		
		return vetor;
	}

	public static int[] CriaVetorDecrescente(int n)
	{
		qntTrocas = 0;
		qntComparacoes = 0; 
		
		int [] vetor = new int[n];
		
		for(int i = 0; i < n; i++)
		{
			vetor[i] = n - i - 1;
		}
		
		return vetor;
	}

}
