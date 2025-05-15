import axios, { type AxiosInstance } from "axios";
import { type User } from "@/assets/types/user";

const API: AxiosInstance = axios.create({
    baseURL: "http://localhost:8000",
});

export interface AuthResponse {
    token: string;
    user: User;
}

export interface LoginPayload {
    username: string;
    password: string;
}

export interface SignupPayload {
    username: string;
    password: string;
}

export function setAuthToken(token: string | null): void {
    if (token) {
        API.defaults.headers.common["Authorization"] = `Bearer ${token}`;
        localStorage.setItem("token", token);
    } else {
        delete API.defaults.headers.common["Authorization"];
        localStorage.removeItem("token");
    }
}

export const setUserId = (userId: number | null) => {
    if (userId) {
        API.defaults.headers.common["UserId"] = String(userId);
        localStorage.setItem("userId", String(userId));
    } else {
        delete API.defaults.headers.common["UserId"];
        localStorage.removeItem("userId");
    }
};

const storedToken = localStorage.getItem("token");
if (storedToken) {
    setAuthToken(storedToken);
}

export async function signup(payload: SignupPayload): Promise<AuthResponse> {
    const response = await API.post("/signup", payload);
    const { token, user } = response.data;
    setAuthToken(token);
    localStorage.setItem("userId", String(user.id));
    return response.data;
}

export async function login(payload: LoginPayload): Promise<AuthResponse> {
    const response = await API.post("/login", payload);
    const { token, user } = response.data;
    setAuthToken(token);
    localStorage.setItem("userId", String(user.id));
    return response.data;
}

export async function testToken(): Promise<boolean> {
    try {
        await API.get("/test_token");
        return true;
    } catch (err) {
        setAuthToken(null);
        return false;
    }
}

export function isLoggedIn(): boolean {
    return localStorage.getItem("token") !== null;
}

export async function logout(): Promise<void> {
    setAuthToken(null);
    setUserId(null);
}
