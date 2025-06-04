package com.example.apptest

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

import android.util.Log
import android.widget.Button
import android.widget.EditText
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import android.text.method.ScrollingMovementMethod


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btnGetData:Button = findViewById(R.id.btnGetData)

        btnGetData.setOnClickListener(){
            fetchItems()
        }

    }
    private fun fetchItems() {
        val call = RetrofitClient.instance.getData()
        val nameContainer:EditText = findViewById(R.id.nameContainer)
        val emailContainer:EditText = findViewById(R.id.emailContainer)

        nameContainer.movementMethod = ScrollingMovementMethod()
        emailContainer.movementMethod = ScrollingMovementMethod()

        call.enqueue(object : Callback<List<DjangoData>> {
            override fun onResponse(call: Call<List<DjangoData>>, response: Response<List<DjangoData>>) {

                if (response.isSuccessful) {
                    val items = response.body()
                    val builderName = StringBuilder()
                    val builderEmail = StringBuilder()

                    items?.forEach {

                        val Name = "${it.fname} ${it.mname} ${it.lname}\n\n\n\n\n\n"
                        val Email = "Email: ${it.email}\nPassword: ${it.password}\nGender: ${it.gender}\nDate of Birth: ${it.dob}\nCourse: ${it.course}\n\n"

                        builderName.append(Name)
                        builderEmail.append(Email)


                    }
                    nameContainer.setText(builderName.toString())
                    emailContainer.setText(builderEmail.toString())


                } else {
                    Log.e("API", "Response failed: ${response.code()}")
                }
            }

            override fun onFailure(call: Call<List<DjangoData>>, t: Throwable) {
                Log.e("API Error", t.message ?: "Unknown error")
            }
        })
    }
}