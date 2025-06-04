package com.example.apptest
import retrofit2.Call
import retrofit2.http.GET

interface appTestAPI {
    @GET("api/users/")
    fun getData(): Call<List<DjangoData>>
}