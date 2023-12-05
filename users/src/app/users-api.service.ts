import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UsersApiService {

  endpoint = 'http://127.0.0.1:3000'

  constructor(
    private http: HttpClient,
  ) { }

  getUsers(): Observable<any> {
    return this.http.get(`${this.endpoint}/users`);
  }

  getUserById(id: number): Observable<any> {
    return this.http.get(`${this.endpoint}/users/${id}`);
  }
  createUser(user: any): Observable<any> {
    return this.http.post(`${this.endpoint}/users`, user);
  }

  updateUser(id: number, user: any): Observable<any> {
    return this.http.put(`${this.endpoint}/users/${id}`, user);
  }

  deleteUserById(id: number): Observable<number> {
    return this.http.delete<number>(`${this.endpoint}/users/${id}`);
  }

}
