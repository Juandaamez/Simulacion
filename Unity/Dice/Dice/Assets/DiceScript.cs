/*__author__       = "Juan David Amezquita Nuñez"
__copyright__    = "Copyright 2023, USTA Tunja"
__credits__      = ["JF Mendoza"]
__license__      = "GPL"
__version__      = "1.0.0"
__maintainer__   = "Juan David Amezquita Nuñez"
__email__        = "juan.amezquita@usantoto.edu.co"
__status__       = "In process"
*/

using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Random = System.Random; // Alias para la clase System.Random

public class DiceScript : MonoBehaviour {

	static Rigidbody rb;
	public static Vector3 diceVelocity;

	// Use this for initialization
	void Start () {
		rb = GetComponent<Rigidbody> ();
	}
	
	// Update is called once per frame
	void Update () {
		diceVelocity = rb.velocity;

		if (Input.GetKeyDown (KeyCode.Space)) {
			int a = 75;
			int c = 0;
			int m = (int)Math.Pow(2, 31) - 1;
			double x = 1;
			int terms = 100;

			DiceNumberTextScript.diceNumber = 0;
			float dirX = random_number(a, c, m, x, terms) * 500;
			float dirY = random_number(a, c, m, x, terms) * 500;
			float dirZ = random_number(a, c, m, x, terms) * 500;
			transform.position = new Vector3 (0, 2, 0);
			transform.rotation = Quaternion.identity;
			rb.AddForce (transform.up * 500);
			rb.AddTorque (dirX, dirY, dirZ);
		}
	}

	static float random_number(int a, int c, int m, double x, int terms){
		List<double> _numbers = new List<double>();

		for (int i = 0; i < terms; i++){
    		x = (a * x + c) % m;
    		_numbers.Add((double)x / m);
		}

		// Seleccionar un número aleatorio de la lista
        double numeroSeleccionado = SeleccionarNumeroAleatorio(_numbers);

		float numeroFinal = (float)numeroSeleccionado;

		return numeroFinal;
	} 

	static double SeleccionarNumeroAleatorio(List<double> _numbers)
    {

		Random random = new Random(); // Crear instancia de Random

        int indiceAleatorio = random.Next(_numbers.Count); // Generar índice aleatorio

        double numeroAleatorio = _numbers[indiceAleatorio]; // Obtener número correspondiente

        return numeroAleatorio;

    }
}
