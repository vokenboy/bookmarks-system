import { ref, computed } from "vue";
import axios, { type AxiosInstance } from "axios";
import { type Workspace } from "@/assets/types/workspace";

const API: AxiosInstance = axios.create({
    baseURL: "http://localhost:8000",
});

export const getWorkspaces = async (userId: number): Promise<Workspace[]> => {
    const response = await API.get<Workspace[]>(`/workspace/user/${userId}/`);
    return response.data;
};

export const getWorkspace = async (id: number): Promise<Workspace> => {
    const response = await API.get<Workspace>(`/workspace/get/${id}/`);
    return response.data;
};

export const createWorkspace = async (
    workspace: Workspace
): Promise<Workspace> => {
    const response = await API.post<Workspace>(`/workspace/add/`, workspace);
    return response.data;
};

export const updateWorkspace = async (
    id: number,
    workspace: Partial<Workspace>
): Promise<Workspace> => {
    const response = await API.put<Workspace>(
        `/workspace/update/${id}/`,
        workspace
    );
    return response.data;
};

export const deleteWorkspace = async (id: number): Promise<void> => {
    await API.delete(`/workspace/delete/${id}/`);
};
