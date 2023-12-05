import { Routes } from '@angular/router';
import { CreateUserComponent } from "./create-user/create-user.component";
import {UsersListComponent} from "./users-list/users-list.component";
import {EditUserComponent} from "./edit-user/edit-user.component";

export const routes: Routes = [
  { path: '', component: UsersListComponent },
  { path: 'create', component: CreateUserComponent },
  { path: 'edit-user/:id', component: EditUserComponent },
];
